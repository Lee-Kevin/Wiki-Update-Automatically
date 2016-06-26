#!/usr/bin/env python
import time 
import subprocess 
import logging
path = "/home/lidreamer/Seeed-WiKi/"
StrUpdate = "Already up-to-date.\n"
cmd  = "git pull"
cmd_mkdocs_serve  = "mkdocs serve"
logging.basicConfig(level='INFO')

def main():
    try:
        data = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,cwd=path).stdout.read()
        logging.info(data)
        if cmp(data,StrUpdate) == 0:
            logging.info("git pull done")
        else:
            logging.info("Need to mkdocs serve") 
            try:
                data = subprocess.Popen(cmd_mkdocs_serve, shell=True, stdout=subprocess.PIPE, cwd=path).stdout.read()
                data.wait()
                logging.info(data)
            except Exception,e:
                logging.warn(e)
    except Exception,e:
        logging.warn(e)
def UpdatetoCloud():
    logging.info("upload to s3 cloud")
    pass
if __name__ == "__main__":
    logging.info("The Code is begining")
    main()


#    retcode = p.wait()
#    print(retcode)
#    try: 
      #  info = subprocess.Popen(cmd1,shell=True,stdout=subprocess.PIPE).stdout.read()
#        info = subprocess.Popen(cmd, shell=True, cwd = path).stdout.read()
#        print(info)
#    except:
#        print("There is something wrong")
