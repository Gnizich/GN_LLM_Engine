import os
import hashlib
from threading import Thread
from pathlib import Path
#import llama_index
from openai import OpenAI
import constants as c
from llama_index import StorageContext, VectorStoreIndex, Document
from llama_index.node_parser import SimpleNodeParser
from llama_index import SimpleDirectoryReader

c.Get_API()
client = OpenAI()

newdocspath = ""
masterpath = ""
basepath = ""
persistpath = ""
indexpath = ""
class Document:
    __slots__ = ['text', 'doc_id', 'id_', 'hash']

    def __init__(self, text: str, doc_id: str):
        self.text = text
        self.doc_id = doc_id
        self.id_ = doc_id
        self.hash = self.generate_hash(text)

    def generate_hash(self, text: str) -> str:
        return hashlib.sha256(text.encode()).hexdigest()

    def get_metadata_str(self, mode=None) -> str:
        return f"{self.doc_id}-{self.hash}"

    def get_content(self, metadata_mode=None) -> str:
        return self.text
def index_document(doc: Document):
    print("index_document reached")
    index = VectorStoreIndex()
    index.add_document(doc)
    print("index doscument complete")

def CreateUpdate_Index(basepath, masterdocs, newdocs, indexpath, action, tool ):
    print('Create/Update function running')

    # Check if index path directory is empty
    main_dir = "."
    indexes_dir = os.path.join(main_dir, "Indexes")
    chkindexpath = os.path.join(indexes_dir, tool)
    print('ckindexpath', chkindexpath)
    index_dir = Path(chkindexpath)
    print('index_dir',index_dir)
    is_empty =len(os.listdir(index_dir)) == 0
    print('is empty', is_empty)
    # if is_empty:
    #     print('Running creating index function')
    #     print(basepath, masterdocs, newdocs, index_dir, tool)
    #     Create_Index(basepath, masterdocs, newdocs, index_dir, tool )
    # else:
    #     print('Running updating index function')
    #     Update_Index(basepath, masterdocs, newdocs, index_dir)
    print('Running creating index function')
    print(basepath, masterdocs, newdocs, index_dir, tool)
    Create_Index(basepath, masterdocs, newdocs, index_dir, tool )

def Create_Index(basepath: str, masterdocs: str, newdocs: str, indexpath: str, tool: str):

    print('Creating index')

    # Load documents
    docpath = masterdocs
    documents = SimpleDirectoryReader(input_dir=docpath).load_data()

    # Parse documents into nodes
    parser = SimpleNodeParser.from_defaults()
    nodes = parser.get_nodes_from_documents(documents)

    # Create index using nodes
    index = VectorStoreIndex(nodes=nodes)
    for doc in documents:
        index.insert(doc)

    # Persist index
    persist_path = os.path.join(basepath, indexpath)
    print('persist_path= ', persist_path)
    saveindexpath = persist_path
    index.storage_context.persist(saveindexpath)

    print('Index created and saved')

def Update_Index(basepath: str, masterdocs: str, newdocs: str, indexpath: str):
    print("update index reached")
    import os
    from llama_index import load_index_from_storage
    print('update_index indexpath', indexpath)

    try:
        is_empty = len(os.listdir(indexpath))
        print('update function is empty', is_empty)
        print('update indexpath= ', indexpath)
        storage_context = StorageContext.from_defaults(indexpath)
        index = load_index_from_storage(storage_context)

        new_docs_dir = os.path.join(basepath, newdocs)
        for filename in os.listdir(new_docs_dir):
            path = os.path.join(new_docs_dir, filename)
            with open(path) as f:
                text = f.read()
            doc = Document(text, filename)
            index.add_document(doc)

        storage_context.persist(index)
        print("Update index completed")
    except Exception as e:
        print(e)
def AskBuild(tool, choice):
    print("AskBuild reached : ", tool, choice)
    if choice == 'build':
        print("Askbuild build reached")
        main_dir = "."
        #train_dir = os.path.join(main_dir, "MyAI_Training_Docs")
        train_dir = ".//MyAI_Training_Docs//"
        train_path = os.path.join(train_dir, tool)
        master_dir = os.path.join(train_path, "Master")
        persistpath = 'Indexes//' + tool + '//'
        if tool == 'ai':
            doc_path = "ai"
        elif tool == 'gn':
            doc_path = "gn"
        newdocspath = train_path + "//Docs"
        masterpath = train_path + "//Master"
        print(tool, choice)
        print("PP: ", persistpath)
        print("nd: ", newdocspath)
        print("mp: ", masterpath)
        #print("bp: ", basepath)
        basepath = ""
        CreateUpdate_Index(basepath, masterpath, newdocspath, persistpath, choice, tool)
        print("Askbuild gn complete")
    elif choice == 'ask':
        print("Askbuild ask reached")
        persistpath = 'Indexes//'
        newdocspath = 'Docs'
        masterpath = 'Master'
        main_dir = "."
        basepath = os.path.join(main_dir, tool)
        indexpath = main_dir + '//Indexes//' + tool + '//'
        AskQuestion(indexpath, persistpath)
        print("Ask build ask complete")
    else:
        pass


def AskQuestion(topic: str, action: str):
    from llama_index import load_index_from_storage
    print(topic)
    print("Ask question reached")
    indexpath = '/home/raspi5/PycharmProjects/GN_LLM_Engine/Indexes/gn' #.//Indexes//' + topic + '//'
    print('indexpath= ', indexpath)
    print(os.listdir(indexpath))
    storage_context = StorageContext.from_defaults(persist_dir=indexpath)
    #storage_context = StorageContext.from_defaults(indexpath)
    #index = load_index_from_storage(storage_context)

    #Load index from the storage context
    new_index = load_index_from_storage(storage_context)

    new_query_engine = new_index.as_query_engine()

    while True:
        question = input("Enter question: ")
        if question.lower() == "exit":
            break
        response = new_query_engine.query(question)
        print(response)

        # response = index.query(question)
        # print(response)
        print("AskQuestion complete")
        return response

AskBuild('gn', 'build')
