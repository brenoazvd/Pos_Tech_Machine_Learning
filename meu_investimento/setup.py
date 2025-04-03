from setuptools import setup, find_packages

setup(
    name='meu_investimento',
    version='0.1',
    packages=find_packages(),  # Aqui está o nome correto
    install_requires=[],
    author='Breno Rodrigues Azevedo',
    author_email='brenorazevedo@hotmail.com',
    description='Uma biblioteca para cálculos de investimentos',
    url='https://github.com/brenoazvd/Pos_Tech_Machine_Learning/tree/main/meu_investimento',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
