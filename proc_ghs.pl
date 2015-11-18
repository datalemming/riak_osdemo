#! /usr/bin/perl

###
#This iterates through the list of bboxes and geohashs
#truncates the geohashes to the required length
#$precision=5 gives a 5km by 5km extent.  See wikipedia
#for further possible values.
#This then outputs to stdout a csv list of 
#TruncatedGeohash,PolygonIndex:PolygonIndex etc \n
#
#SMDE 18/11/15
###

use File::Slurp;
use Modern::Perl;
use Data::Dumper;

my @lines=read_file('boxes-and-hashes.csv');
my %ghs;
my ($line, $index, $gh, $truncgh, $vals, $vals1);
my $precision=5; #can be changed for other extents, see wikipedia for table

foreach $line (@lines) {
	#say $line;
	($index,$gh)=split(/,/,$line);
	$truncgh=substr($gh,0,$precision);
	#say $truncgh;	
	if (exists($ghs{$truncgh})) {
		#call value and add to it
		$vals=$ghs{$truncgh};
		#say $vals;
		$vals1=$index.":".$vals;
		#say $vals1;
		$ghs{$truncgh}=$vals1;	
	} else {
		#add value and key to hash
		$ghs{$truncgh}=$index;
		}
}

#write out hash
print map {"$_,$ghs{$_}\n"} keys %ghs;

