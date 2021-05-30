#apache_beam
from apache_beam.options.pipeline_options import PipelineOptions
import apache_beam as beam

pipeline_options = PipelineOptions(
    project='fluid-crane-284202',
    runner='dataflow',
    temp_location='gs://dataflow-sample-ig/temp2'
)
def pardo_dofn_methods_basic(test=None):
    import apache_beam as beam
    def normalize_and_validate_category(categories_list, valid_category):

        categories_list['category'] = categories_list['category'].lower()
        if categories_list['category'] in valid_category :
            yield categories_list

    def generate_elements(text):
        pre_processing = []
        for word in text.split(","):
            pre_processing.append(word)
        yield pre_processing

    def toString(text) :
        csvFormat = ''
        for category, nested in text.items():
            for language in nested:
                csvFormat += (category + "," + language + "," + str(nested[language]) + ",")
        yield csvFormat

    class maketablerow(beam.DoFn):
        #init 에 delimiter 생성하기
        def __init__(self, delimiter=','):
            self.delimiter = delimiter

        def process(self, element):
            #하나의 문자열로 처리되서 그렇다.

            if element is not None:
                #for i in range(len(element)) :
                    splited = element.split(self.delimiter)

                    array_index = 0
                    for splited_index in range(int(len(splited)/3)) :
                        tablerow = {
                            'category' : splited[array_index],
                            'language' : splited[array_index+1],
                            'count' : splited[array_index+2]
                        }
                        yield tablerow
                        array_index = array_index + 3

    class split_category_basic(beam.DoFn):
      def __init__(self, delimiter=','):
        self.delimiter = delimiter
        self.k = 1
        self.pre_processing = []
        self.window = beam.window.GlobalWindow()
        self.category_dict = {}
        self.category_index = 0
        self.language_index = 1

      def setup(self):
          print('setup')

      def start_bundle(self):
          print('start_bundle')

      def finish_bundle(self):
          # category 를 우선 배정
          print('finish_bundle')

          for ppc_index in range(len(self.pre_processing)) :
              if self.category_index == 0 or self.category_index%3 == 0 :
                  # dict에 포함되어있는 category 인지 확인
                  if self.pre_processing[self.category_index] not in self.category_dict :
                      self.category_dict[self.pre_processing[self.category_index]] = {}

              # language 가 몇번 나왔는지 wordCount
              if ppc_index + 1 == 1 or ppc_index + 1 == self.language_index:
                  language = self.pre_processing[self.language_index].split(' ')
                  for lang_index in range(len(language)) :
                    if language[lang_index] not in self.category_dict[self.pre_processing[self.category_index]] :
                        self.category_dict[self.pre_processing[self.category_index]][language[lang_index]] = 1
                    else :
                        self.category_dict[self.pre_processing[self.category_index]][language[lang_index]] += 1
                  self.language_index = self.language_index + 3;  # next language location

              self.category_index = self.category_index + 1



          yield beam.utils.windowed_value.WindowedValue(
              value=self.category_dict,
              timestamp=0,
              windows=[self.window],
          )

      def process(self, text):
         self.pre_processing.extend(text)


    with beam.Pipeline(options=pipeline_options) as pipeline:
      valid_category = pipeline | 'pre-processing : Valid durations' >> beam.Create([
          'web', 'iot', 'cloud', 'data', 'server', 'client', 'app', 'firmware', 'ai', 'network', 'blockchain', 'game',
          'db', 'security'
      ])

      pre_processing = (
          pipeline
          | 'Extract : Read Bucket' >> beam.io.ReadFromText("gs://external_source_bucket/output.csv",
                                                            skip_header_lines=1)
          | 'Pre_processing : Data generate' >> beam.FlatMap(generate_elements) # data generate
          | 'Pre_processing : Split category basic' >> beam.ParDo(split_category_basic(','))
          | 'Pre_processing : dict()->str' >>beam.FlatMap(toString)
      )

      Loading = (pre_processing
         | 'Loading : bigQuery : make table row for bigQuery' >> beam.ParDo(maketablerow(','))
         | 'Loading : Normalize and validate category'>> beam.FlatMap(
                  normalize_and_validate_category,
                  valid_category = beam.pvalue.AsIter(valid_category)
              )
        #  | beam.Map(print)
         | 'Loading : bigQuery extract' >> beam.io.WriteToBigQuery(
                  'fluid-crane-284202:testdataset.temp_test1',
                  schema='category:STRING, language:STRING, count:STRING',
                  create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
                  write_disposition=beam.io.BigQueryDisposition.WRITE_TRUNCATE
        )
        )

    if test:
        return test(pre_processing)

if __name__ == '__main__' :
    pardo_dofn_methods_basic()