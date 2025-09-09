#for installing local packages in virtual environment
from setuptools import find_packages, setup

setup(
    name="mcqgenerator",
    version="0.0.1",
    author="Kumar Kushagra",
    author_email="kumarkushagra09@gmail.com",
    description="A package for generating MCQs using OpenAI, LangChain, Hugging Face, and Streamlit",
    packages=find_packages(),
    install_requires=[
        "openai",
        "langchain",
        "streamlit",
        "python-dotenv",
        "PyPDF2",
        "huggingface_hub",
        "torch",
        "torchvision",
        "torchaudio",
        "transformers",
        "tensorflow"
    ],
)
