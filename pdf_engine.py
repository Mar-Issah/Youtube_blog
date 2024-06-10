import os
from llama_index.core import StorageContext, VectorStoreIndex, load_index_from_storage
# PDFReader to read unstructures data i.e pdf file
from llama_index.readers.file import PDFReader
import os

# this fxn accepts the document to persist and the path
def get_index(docs, index_path):
	index = None
	# if the path exist then docs has been persisted then we simply load from the staorage
	if not os.path.exists(index_path):
		print(index_path)
		index = VectorStoreIndex.from_documents(docs, show_progress=True)
		index.storage_context.persist(persist_dir=index_path)
	else:
		index = load_index_from_storage(StorageContext.from_defaults(persist_dir	=index_path))
	return index


loader = PDFReader()
docs = loader.load_data(file=("./data/Africa.pdf"))
search_index = get_index(docs, "./data/index")
africa_query_engine = search_index.as_query_engine()
# print(docs)
