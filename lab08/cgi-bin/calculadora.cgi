#!"C:/xampp/perl/bin/perl.exe"

use strict;
use warnings;
use CGI;

my $q = CGI->new;
my $expresion = $q->('expresion');
chomp $expresion;
my $resultado;

