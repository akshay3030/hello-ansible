#!/usr/bin/python

#from ansible.module_utils.basic import *
import fnmatch
import json
import os
import shlex
import sys
from bson import json_util

def main():
    """ Entry point for the module """

    #Ansible stores arguments in file and passes that file to the module
    argument_file = sys.argv[1]
    argument_content = file(argument_file).read()
    #arguments = shlex.split(argument_content)
    #formatted_json_string=json.dumps(argument_content,default=json_util.default)

    parsed_json = json.loads(str(argument_content))

	#Json Parsing
    #directory = parsed_json["ANSIBLE_MODULE_ARGS"]["dir"]
    try:
        directory = parsed_json["ANSIBLE_MODULE_ARGS"]["dir"]
    except:
        #directory = "."
        print json.dumps({
        'failed' : True,
        'msg' : 'dir is required'
        })
        sys.exit(1)
    try:
        extension = parsed_json["ANSIBLE_MODULE_ARGS"]["ext"]
    except:
        extension = "*.py"

    file_count = len([os.path.join(dirpath, f)
                      for dirpath, _, files in os.walk(directory)
                      for f in fnmatch.filter(files, extension)])
    #print "file count : " + str(file_count)

    print json.dumps({
        "dir": "directory",
        "ext": extension,
        "file_count": file_count
        })

if __name__ == '__main__':
    main()




    # if not str(parsed_json["ANSIBLE_MODULE_ARGS"]["dir"]):
    #     directory= "."
    # else:
    #     directory = str(parsed_json["ANSIBLE_MODULE_ARGS"]["dir"])
    #
    # if not str(parsed_json["ANSIBLE_MODULE_ARGS"]["ext"]):
    #     extension= "*.py"
    # else:
    #     extension = str(parsed_json["ANSIBLE_MODULE_ARGS"]["ext"])



    # arguments_dict = {}
    # for argument in arguments:
    #     print argument
    #     if "=" in argument:
    #         name, value = argument.split('=')
    #         #obvisouly crude, however works for a demo
    #         arguments_dict[name] = value
    #         print arguments_dict
    #
    # print arguments_dict

    # if not directory or not extension:
    #     print json.dumps({
    #     'failed' : True,
    #     'msg' : 'dir and ext are required'
    #     })
    #     sys.exit(1)
