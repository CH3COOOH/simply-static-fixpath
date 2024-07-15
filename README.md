# simply-static-fixpath
Fix incorrectly encoded path characters of WordPress pages archived by Simply-Static. For Chinese characters.

## What does it do
Name of files and folders archived by Simply-Static are using GB18030 encoding, while it should be UTF8. That means you would see garbled text in filename of archived files with Chinese characters. This tool is aim to convert filenames in those archived files to UTF8.

## Usage
`python3 main.py <root_of_site>`
