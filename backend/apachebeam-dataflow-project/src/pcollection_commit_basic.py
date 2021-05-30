#apache_beam
from apache_beam.options.pipeline_options import PipelineOptions
import apache_beam as beam

pipeline_options = PipelineOptions(
    project='fluid-crane-284202',
    runner='dataflow',
    temp_location='gs://dataflow-sample-ig/temp2'
)

def pcollection_dofn_methods_basic(test=None):
    import apache_beam as beam
    def make_tablerow(element) :
        if element is not None :
            splited = element.split(',')
            array_index = 0
            for splited_index in range(int(len(splited)/4)) :
                tablerow = {
                    'category' : splited[array_index],
                    'language' : splited[array_index+1],
                    'commit' : splited[array_index+2],
                    'language_bytes' : splited[array_index+3],
                }
                yield tablerow
                array_index = array_index + 4

    def toString(text) :
        csvFormat = ''
        for category, nested in text.items():
            for commit, two_nested in nested.items():
                two_nested['language_bytes'] = round(two_nested['language_bytes'],3)
                csvFormat += (category + "," + commit + "," + str(two_nested['commit']) + "," + str(two_nested['language_bytes'])+",")
        yield csvFormat

    class generate_key_value(beam.DoFn) :
        def __init__(self, delimiter=','):
            self.delimiter = delimiter
            self.pre_processing = []
            self.window = beam.window.GlobalWindow()

        def process(self, text):
            self.pre_processing.append(text)

        def finish_bundle(self):
            dict = {}
            for i in range(len(self.pre_processing)) :
                split = self.pre_processing[i].split(',')
                if split[0] not in dict :
                    dict[split[0]] = {}
            for i in range(len(self.pre_processing)) :
                split = self.pre_processing[i].split(',')
                if split[1] not in dict[split[0]] :
                    dict[split[0]][split[1]] ={}

            # for i in range(len(self.pre_processing)) :
            #    split = self.pre_processing[i].split(',')
            #    if not dict[split[0]][split[1]]:
            #        dict[split[0]][split[1]]={}

            for i in range(len(self.pre_processing)) :
                split = self.pre_processing[i].split(',')
                tempi = int(split[2])
                tempj = float(split[3])
                if not dict[split[0]][split[1]] :
                    dict[split[0]][split[1]]['commit'] = tempi
                    dict[split[0]][split[1]]['language_bytes'] = tempj
                else :
                    dict[split[0]][split[1]]['commit'] += tempi
                    dict[split[0]][split[1]]['language_bytes'] += tempj

            print(self.pre_processing)
            yield beam.utils.windowed_value.WindowedValue(
                value=dict,
                timestamp=0,
                windows=[self.window],
            )
    with beam.Pipeline(options=pipeline_options) as pipeline:
    #with beam.Pipeline() as pipeline:
        p1 = (
             pipeline
            | 'Extract:bucket' >> beam.io.ReadFromText("gs://external_source_bucket/commit_output.csv",
                                                skip_header_lines=1)
            | 'Transform:split-category'>>beam.ParDo(generate_key_value(","))
            | 'Transform:toString'>>beam.FlatMap(toString)
        )
        p2 = (
            p1
            | 'Loading:table' >> beam.ParDo(make_tablerow)
            # | 'map' >> beam.Map(print)
            | 'Loading:bigquery'>>beam.io.WriteToBigQuery(
            'fluid-crane-284202:prototyping_dataset.commit_basic',
            schema='category:STRING, language:STRING, commit:STRING, language_bytes:STRING',
            create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
            write_disposition=beam.io.BigQueryDisposition.WRITE_TRUNCATE
        )

        )


if __name__ == '__main__' :
    pcollection_dofn_methods_basic()