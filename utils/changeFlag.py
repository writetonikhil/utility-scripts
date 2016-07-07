import sys
import os
import winioctlcon

def change(n):
    ch = ""
    if n & winioctlcon.USN_PAGE_SIZE :
        ch = ch + "," + "PAGE_SIZE "
    if n & winioctlcon.USN_REASON_DATA_OVERWRITE :
        ch = ch + "," + "DATA_OVERWRITE  "
    if n & winioctlcon.USN_REASON_DATA_EXTEND :
        ch = ch + "," + "DATA_EXTEND "
    if n & winioctlcon.USN_REASON_DATA_TRUNCATION :
        ch = ch + "," + "DATA_TRUNCATION  "
    if n & winioctlcon.USN_REASON_NAMED_DATA_OVERWRITE  :
        ch = ch + "," + "NAMED_DATA_OVERWRITE  "
    if n & winioctlcon.USN_REASON_NAMED_DATA_EXTEND  :
        ch = ch + "," + "NAMED_DATA_EXTEND "
    if n & winioctlcon.USN_REASON_NAMED_DATA_TRUNCATION  :
        ch = ch + "," + "NAMED_DATA_TRUNCATION  "
    if n & winioctlcon.USN_REASON_FILE_CREATE  :
        ch = ch + "," + "FILE_CREATE  "
    if n & winioctlcon.USN_REASON_FILE_DELETE  :
        ch = ch + "," + "FILE_DELETE  "
    if n & winioctlcon.USN_REASON_EA_CHANGE  :
        ch = ch + "," + "EA_CHANGE  "
    if n & winioctlcon.USN_REASON_SECURITY_CHANGE  :
        ch = ch + "," + "SECURITY_CHANGE  "
    if n & winioctlcon.USN_REASON_RENAME_OLD_NAME  :
        ch = ch + "," + "RENAME_OLD_NAME  "
    if n & winioctlcon.USN_REASON_RENAME_NEW_NAME  :
        ch = ch + "," + "RENAME_NEW_NAME  "
    if n & winioctlcon.USN_REASON_INDEXABLE_CHANGE  :
        ch = ch + "," + "INDEXABLE_CHANGE  "
    if n & winioctlcon.USN_REASON_BASIC_INFO_CHANGE  :
        ch = ch + "," + "BASIC_INFO_CHANGE  "
    if n & winioctlcon.USN_REASON_HARD_LINK_CHANGE  :
        ch = ch + "," + "HARD_LINK_CHANGE  "
    if n & winioctlcon.USN_REASON_COMPRESSION_CHANGE  :
        ch = ch + "," + "COMPRESSION_CHANGE "
    if n & winioctlcon.USN_REASON_ENCRYPTION_CHANGE  :
        ch = ch + "," + "ENCRYPTION_CHANGE  "
    if n & winioctlcon.USN_REASON_OBJECT_ID_CHANGE  :
        ch = ch + "," + "OBJECT_ID_CHANGE  "
    if n & winioctlcon.USN_REASON_REPARSE_POINT_CHANGE  :
        ch = ch + "," + "REPARSE_POINT_CHANGE "
    if n & winioctlcon.USN_REASON_STREAM_CHANGE  :
        ch = ch + "," + "STREAM_CHANGE  "
    if n & winioctlcon.USN_REASON_TRANSACTED_CHANGE  :
        ch = ch + "," + "TRANSACTED_CHANGE  "
    if n & winioctlcon.USN_REASON_CLOSE :
        ch = ch + "," + "CLOSE  "
    if n & winioctlcon.USN_DELETE_FLAG_DELETE  :
        ch = ch + "," + "FLAG_DELETE  "
    if n & winioctlcon.USN_DELETE_FLAG_NOTIFY  :
        ch = ch + "," + "FLAG_NOTIFY  "
    if n & winioctlcon.USN_DELETE_VALID_FLAGS  :
        ch = ch + "," + "VALID_FLAGS "
    if n & winioctlcon.USN_SOURCE_DATA_MANAGEMENT  :
        ch = ch + "," + "DATA_MANAGEMENT  "
    if n & winioctlcon.USN_SOURCE_AUXILIARY_DATA :
        ch = ch + "," + "AUXILIARY_DATA  "
    if n & winioctlcon.USN_SOURCE_REPLICATION_MANAGEMENT  :
        ch = ch + "," + "REPLICATION_MANAGEMENT  "
    return ch

if __name__ == '__main__':
    changeNo = int(sys.argv[1])
    print change(changeNo)
   