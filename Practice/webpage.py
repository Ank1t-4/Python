#Command line utility to download a web page and save it to a file as HTML or convert it to PDF
import os
import requests
import argparse
import asyncio
from playwright.async_api import async_playwright

os.system('cls')

def name_for_file(local_filename,type):
    if local_filename == 'output' and type=='pdf':
        local_filename = 'output' + '.pdf'#os.path.basename(url)
    elif local_filename=='output' and type=='html':
            local_filename = 'Newfile.html'

    i=0
    j=0
    while True:
        if os.path.exists(f'E:/My Programs/Temp/{local_filename}'):
            if local_filename.endswith(f'({i+1}).html') :
                print(local_filename)
                i+=1
                local_filename = local_filename[:-8] + str(f'({i+1})') + local_filename[-5:]
            
            elif local_filename.endswith(f'({j+1}).pdf') :
                print(local_filename)
                j+=1
                local_filename = local_filename[:-7] + str(f'({j+1})') + local_filename[-4:]
            
            while local_filename.endswith('.html') and i==0:
                local_filename = local_filename[:-5] + str(f'({i+1})') + local_filename[-5:]
                break
            while local_filename.endswith('.pdf') and j==0:
                local_filename = local_filename[:-4] + str(f'({j+1})') + local_filename[-4:]
                break
        else:break
    return local_filename

def download_file(url, local_filename):
    '''Download a webpage and save it to a file as HTML'''
    with requests.get(url) as r:
        with open(f'E:/My Programs/Temp/{local_filename}', 'wb') as f:
            f.write(r.content)
            return f

async def convert_to_pdf(url, output_path):
    '''Convert a webpage to PDF'''
    output_path = f'E:/My Programs/Temp/{output_path}'
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(url, timeout=60000)
        await page.pdf(path=output_path)
        await browser.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='URL of the webpage to download')
    parser.add_argument('-o', '--output', help='Output file name', default='output')
    parser.add_argument('-p', '--pdf', help='Convert to PDF', action='store_true')

    args = parser.parse_args()
    if args.pdf==True:
        args.output = name_for_file(args.output,type='pdf')
        asyncio.run(convert_to_pdf(args.url, args.output))
    elif args.pdf==False:
        args.output = name_for_file(args.output,type='html')
        html_file = download_file(args.url, args.output)
        print(html_file.name)

    print(args)
if __name__ == "__main__":
    main()