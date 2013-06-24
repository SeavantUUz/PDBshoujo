#!env/bin/python
# coding:utf-8

import optparse
from appleSouffle import post,remove,postAll,show,init,updateThemes

def _parserInput():
    parser = optparse.OptionParser(version="%prog 0.1")
    parser.add_option("--init",action = "store_true",dest="init",help='init environment')
    parser.add_option("--show",action = "store_true",dest="show",help='Show all posts you post')
    parser.add_option("--remove",action = "store",type="int",default = None,dest="remove",help="Remove a node.ex: --remove=3")
    parser.add_option("--post",action = "store",default = None,dest="post",help="Submit your post.ex: --post=filename")
    parser.add_option("--postAll",action ="store",default=None,dest="postAll",help='Rebuild all posts,you can pass a dirname,or notion .Pass 0 to it will set rebuild from backup dir.ex: --postAll=0 or --postAll=/home/xxx')
    parser.add_option("--updateThemes",action = "store_true",dest="updateThemes",help='Update all of your themes.Each time you add a new theme and you should run it')

    options,remainder = parser.parse_args()

    return options

def main():
    options = _parserInput()
    if options.init:
        init()
    elif options.post!= None:
        post(options.post)
    elif options.remove!=None:
        remove(options.remove)
    elif options.show:
        show()
    elif options.postAll != None:
        if options.postAll == '0':
            postAll()
        else:
            postAll(options.postAll)
    elif options.updateThemes:
        updateThemes()

if __name__ == "__main__":
    main()
