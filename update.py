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
                child = subprocess.Popen(cmd_mkdocs_serve, shell=True, stdout=subprocess.PIPE, cwd=path)
                time.sleep(10)
                child.kill()
                logging.info("Kill the childprocess")
                kill_process("mkdocs")
            except Exception,e:
                logging.warn(e)
    except Exception,e:
        logging.warn(e)
def UpdatetoCloud():
    logging.info("upload to s3 cloud")
    pass

def kill_process(name):
    cmd_temp = "ps aux | grep %s" % name
    data = subprocess.Popen(cmd_temp,shell=True, stdout=subprocess.PIPE).stdout.read()
    logging.info(data)
    colum = data.split()
    cmd_temp = "kill %d" % int(colum[1])
    data = subprocess.Popen(cmd_temp,shell=True, stdout=subprocess.PIPE).stdout.read()
    logging.info(data)


if __name__ == "__main__":
    logging.info("The Code is begining")
    kill_process("mkdocs")
    while(True):
        main()
        time.sleep(5)


#    retcode = p.wait()
#    print(retcode)
#    try: 
      #  info = subprocess.Popen(cmd1,shell=True,stdout=subprocess.PIPE).stdout.read()
#        info = subprocess.Popen(cmd, shell=True, cwd = path).stdout.read()
#        print(info)
#    except:
#        print("There is something wrong")
