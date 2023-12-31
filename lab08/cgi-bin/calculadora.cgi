#!"C:/xampp/perl/bin/perl.exe"

use strict;
use warnings;
use CGI;

my $q = CGI->new;
my $expresion = $q->('expresion');
chomp $expresion;
my $resultado;

if($expresion=~/[0-9\*\+\/\^\-\(\)]/){
	while($expresion=~m/\((\d+)(.)(\d+)\)/){
      $resultado=calcular($1,$2,$3);
      $expresion=~s/\(($1).($3)\)/$resultado/;
   }
   while($expresion=~m/(\d+)(\*|\/)(\d+)/){
      $resultado=calcular($1,$2,$3);
      $expresion=~s/($1).($3)/$resultado/;
   }
   while($expresion=~m/(\d+)(.)(\d+)/){
      $resultado=calcular($1,$2,$3);
      $expresion=~s/($1).$3/$resultado/;
   }
}
