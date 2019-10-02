import re
import csv
import sys

from subprocess import call

billing_cycle_date = re.compile(r'(\d{,2}/\d{,2}/\d{,2}-\d{,2}/\d{,2}/\d{,2})')
billing_cycle_date_new = re.compile(r'Issue Date:([A-z]{3}|[A-z]{19})\s+(\d{1,}), (\d{2,4})')
indivial_cell_fee = re.compile(r'Total for(\d\d\d \d\d\d-\d\d\d\d)(\d*\.\d*)(CR| )')
indivial_cell_fee_new = re.compile(r'Total for\s*(\d\d\d.\d\d\d.\d\d\d\d)(\$\d*\.\d*)')
indivial_cell = re.compile(r'(\d\d\d \d\d\d-\d\d\d\d)')
data_fee = re.compile(r'1\.Mobile Share Value \d+GB with Rollover Data(\d+\.\d*)')


def ParseBillPDF():
    call(["pdf2txt.py", "-t", "tag", "-o", "output", sys.argv[1]])
    f = open("output")
    raw = f.read()
    searchObj = indivial_cell_fee.findall(raw)
    d = billing_cycle_date.findall(raw)
    date = next(iter(set(d)))
    data = data_fee.findall(raw)
    f.close()

    with open('billing_cycle_date.csv', 'w') as bcd:
        writer =  csv.writer(bcd)
        writer.writerow([date])

    with open('RawData.csv','w') as wf:
        writer = csv.writer(wf)
        if searchObj:
            for item in searchObj:
                print item
				phone = item[0].replace('-', '').replace(' ','')
                writer.writerow((item[0], phone, item[1], item[2]))
        else:
            print "No match!"


def main():
    if len(sys.argv) != 2:
        print "Format: " + sys.argv[0] + " [PDF file]"
        sys.exit()
    ParseBillPDF()


if __name__ == '__main__':
    main()