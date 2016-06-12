import csv
import sys
import vcf


file = open("accepted.txt", "w")
vcf_reader = vcf.Reader(open('C:\Users\Salman\Documents\GitHub\Assignment\Problem 1\mutect_immediate.vcf', 'r'))

total=0

with open('accepted.csv', 'w') as csvfile:
	fieldnames = ['Record CHROM', 'Record POS', 'Record REF', 'Record ALT', 'Region CHROM', 'Region START', 'Region END','FILTER']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
				

for record in iter(vcf_reader):
	f = open("C:/Users/Salman/Documents/GitHub/Assignment/Problem 1/truseq.bed", "r")
	for line in iter(f):
		words=line.split('\t')
		start = words[1]
		end = words[2]
		for i in range(long(start),long(end)+1):
			if(i==record.POS):
				print("\n\nMatch found");
				print record
				print line
				
				file.write("\nMatch found\n")
				file.write(str(record) + "\n")
				file.write("Region\t "+str(line) + "\n")
				
				with open('accepted.csv', 'a') as csvfile:
					fieldnames = ['Record CHROM', 'Record POS', 'Record REF', 'Record ALT', 'Region CHROM', 'Region START', 'Region END','FILTER']
					writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
					#writer.writeheader()
					writer.writerow({'Record CHROM': record.CHROM, 'Record POS': record.POS, 'Record REF': record.REF, 'Record ALT': record.ALT, 'Region CHROM': words[0], 'Region START': words[1], 'Region END': words[2],'FILTER':'PASS'})
		
				
				total=total+1;
	f.close()

print("\nTotal matches found=");
print(total);
file.write("\n\n\n---------------------------------------------------------------------------------------")
file.write("\nTotal matches found = ")
file.write(str(total))
file.close()


