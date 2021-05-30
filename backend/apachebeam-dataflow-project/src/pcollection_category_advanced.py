#apache_beam
from apache_beam.options.pipeline_options import PipelineOptions
import apache_beam as beam

pipeline_options = PipelineOptions(
    project='fluid-crane-284202',
    runner='dataflow',
    temp_location='gs://dataflow-sample-ig/temp2'
)
def pardo_dofn_methods(test=None):
    import apache_beam as beam
    def make_tablerow(element) :
        if element is not None :
            splited = element.split(',')
            array_index = 0
            for splited_index in range(int(len(splited)/4)) :
                tablerow = {
                    'category' : splited[array_index],
                    'year' : splited[array_index+1],
                    'language' : splited[array_index+2],
                    'count' : splited[array_index+3],
                }
                yield tablerow
                array_index = array_index + 4

    def toString(text) :
        csvFormat = ''
        for category, nested in text.items():
            for year in nested:
                for language in nested[year]:
                    csvFormat += (category + "," + str(year) + "," + language + "," + str(nested[year][language]) + ",")
        yield csvFormat


    class split_category_advanced(beam.DoFn):
      def __init__(self, delimiter=','):
        self.delimiter = delimiter
        self.k = 1
        self.pre_processing = []
        self.window = beam.window.GlobalWindow()
        self.year_dict = {}
        self.category_index = 0
        self.language_index = 1
        self.year_index = 2;
        self.result = []

      def setup(self):
          print('setup')

      def start_bundle(self):
          print('start_bundle')

      def finish_bundle(self):
          # category 를 우선 배정
          print('finish_bundle')
          for ppc_index in range(len(self.pre_processing)) :
              if self.category_index == 0 or self.category_index%3 == 0 :
                  if self.pre_processing[self.category_index] not in self.year_dict :
                      self.year_dict[self.pre_processing[self.category_index]] = {}

              # year 별로 어떤 language 가 나오는지 체크
              if ppc_index + 2 == 2 or ppc_index + 2 == self.year_index :
                  # { category : { year : {} } }
                  if self.pre_processing[self.year_index] not in self.year_dict[self.pre_processing[self.category_index]] :
                         self.year_dict[self.pre_processing[self.category_index]][self.pre_processing[self.year_index]] = {}
                  # { category : { year : c : { }, c++ : { }, java : { }}}
                  language = self.pre_processing[self.year_index-1].split(' ')

                  for lang_index in range(len(language)) :
                        if language[lang_index] not in self.year_dict[self.pre_processing[self.category_index]][self.pre_processing[self.year_index]] :
                          self.year_dict[self.pre_processing[self.category_index]][self.pre_processing[self.year_index]][language[lang_index]] = 1
                        else :
                            self.year_dict[self.pre_processing[self.category_index]][self.pre_processing[self.year_index]][
                                language[lang_index]] += 1
                  self.year_index = self.year_index + 3
              self.category_index = self.category_index + 1



          yield beam.utils.windowed_value.WindowedValue(
              value=self.year_dict,
              #value = self.pre_processing,
              timestamp=0,
              windows=[self.window],
          )

      def process(self, text):
        for word in text.split(self.delimiter):
            self.pre_processing.append(word)


    with beam.Pipeline(options=pipeline_options) as pipeline:
      results = (
          pipeline
          | 'Read' >> beam.io.ReadFromText("gs://external_source_bucket/output.csv", skip_header_lines=1)
          | 'Split category advanced' >> beam.ParDo(split_category_advanced(','))
          | 'toString' >> beam.FlatMap(toString)
          | 'setTable' >> beam.ParDo(make_tablerow)
          | beam.io.WriteToBigQuery(
                  'fluid-crane-284202:prototyping_dataset.category_advanced',
                  schema='category:STRING, year:STRING, language:STRING, count:STRING',
                  create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
                  write_disposition=beam.io.BigQueryDisposition.WRITE_TRUNCATE
        )
      )
    if test:
        return test(results)

if __name__ == '__main__':
    pardo_dofn_methods()