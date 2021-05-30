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
    class generate_key_value(beam.DoFn) :
        def __init__(self, delimiter=','):
            self.delimiter = delimiter
            self.pre_processing = []
            self.window = beam.window.GlobalWindow()

        def process(self, text):
            return self.pre_processing.append(text)


        def finish_bundle(self):
            dict = {}

            for i in range(len(self.pre_processing)):
                split = self.pre_processing[i].split(',')
                if split[0] not in dict :
                    dict[split[0]] = {}

            for i in range(len(self.pre_processing)):
                split = self.pre_processing[i].split(',')
                if split[1] not in dict[split[0]] :
                    dict[split[0]][split[1]] = {}

            for i in range(len(self.pre_processing)) :
                split = self.pre_processing[i].split(',')
                tempi = int(split[2])
                if 'score' not in dict[split[0]][split[1]] :
                    dict[split[0]][split[1]]['score'] = tempi
                    dict[split[0]][split[1]]['count'] = 1
                else :
                    dict[split[0]][split[1]]['score'] = dict[split[0]][split[1]]['score'] + tempi
                    dict[split[0]][split[1]]['count'] += 1


            yield beam.utils.windowed_value.WindowedValue(
                value=dict,
                timestamp=0,
                windows=[self.window],
            )
    def generate_key(element, delimiter=',') :
        splited = element.split(delimiter)
        #splited[1] = splited[1][1:]

        return [(f"{splited[0]},{splited[1]}", int(splited[2]))]

    def toString(text) :
        if text is not None :
            csvFormat = ''
            for category, nested in text.items():
                for feature, two_nested in nested.items():
                    csvFormat += (category + "," + feature + "," + str(two_nested['score']) + "," +str(two_nested['count'])+",")
            yield csvFormat

    def make_tablerow(element):
        yield element
    def generate_value(element):
        element_list = list(element)
        splited = element[0].split(',')
        splited[1] = splited[1][1:]
        return [(f"{splited[0]}, {splited[1]}, {element_list[1]}",1)]

    def make_tablerow(element) :

        if element is not None :
            splited = element.split(',')
            array_index = 0
            for splited_index in range(int(len(splited)/4)) :
                tablerow = {
                    'category' : splited[array_index],
                    'feature' : splited[array_index+1],
                    'score' : splited[array_index+2],
                    'count' : splited[array_index+3],
                }
                yield tablerow
                array_index = array_index +4

    with beam.Pipeline(options=pipeline_options) as pipeline:
        p1 = (
            pipeline
            | 'Extract:bucket' >> beam.io.ReadFromText("gs://external_source_bucket/feature_output.csv",
                                                            skip_header_lines=1)
            | 'Transform:split'>>beam.ParDo(generate_key_value(','))
            | 'Transform:toString'>>beam.FlatMap(toString)
        )
        p2 = (
            p1
            | 'Loading:table' >> beam.ParDo(make_tablerow)
            | 'Loading:bigQuery'>>beam.io.WriteToBigQuery(
                  'fluid-crane-284202:prototyping_dataset.feature_basic',
                  schema='category:STRING, feature:STRING, score:STRING, count:STRING',
                  create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
                  write_disposition=beam.io.BigQueryDisposition.WRITE_TRUNCATE
        )
        )


if __name__ == '__main__' :
    pcollection_dofn_methods_basic()