#!/usr/bin/perl

#test riak

use Net::Riak;
use Modern::Perl;

my $client=Net::Riak->new(
	transport=>'PBC',
	host=>'127.0.0.1',
	port=>8087
	);
if (!$client->is_alive){
	say "Riak Client Issues";
	} else {
		say "Client's alive, alive, alive";
	}
	
	
	

