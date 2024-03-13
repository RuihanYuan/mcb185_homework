import argparse
import gzip


#process vcf file
def parse_vcf(vcf_file):
	variants = []
	with gzip.open(vcf_file, 'rt') as fp:
		for line in fp:
			if not line.startswith('#'):
				line = line.strip().split('\t')
				chrom = line[0]
				pos = int(line[1])
				variants.append((chrom, pos))
	return variants

#parse gff
def parse_gff(gff_file):
	region = []
	with gzip.open(gff_file, 'rt') as fp:
		for line in fp:
			if line.strip() and not line.startswith('#'):
				cols = line.strip().split('\t')
				chrom = cols[0]
				feature_type = cols[2]
				start_pos = int(cols[3])
				end_pos = int(cols[4])
				region.append((chrom, start_pos, end_pos, feature_type))
	return region
	
def find_variant(vcf_pos, gff_reg):
	for chrom, pos in vcf_pos:
		feature = []
		for f_chrom, start, end, feature_type in gff_reg:
			if chrom == f_chrom and start <= pos <= end:
				if feature_type not in feature:
					feature.append(feature_type)
		if feature:
			print(f"{chrom}\t{pos}\t{','.join(sorted(feature))}")

parser = argparse.ArgumentParser(description='variant reporter')
parser.add_argument('gff', type=str, help='GFF file')
parser.add_argument('vcf', type=str, help='VCF file')
arg = parser.parse_args()
vcf_pos = parse_vcf(arg.vcf)
gff_reg = parse_gff(arg.gff)
find_variant(vcf_pos, gff_reg)
