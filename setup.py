from setuptools import find_packages,setup


setup (

 name = 'mcqgenerator',
 version= '0.0.1',
 author = 'abcd',
 author_email= 'xyz@gmail.com',
 install_requires= ["OpenAI","langchain","PyPDF2","streamlit","python-dotenv"],
 packages=find_packages(),
)