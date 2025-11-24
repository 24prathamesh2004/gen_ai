from langchain_community.document_loaders import CSVLoader

loader=CSVLoader(file_path='D:/Langchain/Langchain Document Loaders/bank_data.csv')

docs=loader.load()

print(len(docs))

print(docs[0])