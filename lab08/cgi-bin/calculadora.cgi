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

sub calcular{
      (my $num1,my $oper,my $num2)=@_;
      my $result;

      if($oper eq '+'){
         $result=$num1+$num2;
      } elsif($oper eq '-') {
         $result=$num1-$num2;
      } elsif($oper eq '*'){
         $result=$num1*$num2;
      } elsif($oper eq '^'){
	      $result = 1;
         for (my $i = 1; $i <= $num2; $i++){
            $result *= $num1;
         }
      } else{
         $result=$num1/$num2;
      }
  return ($result);
}

print $q->header('text/html');
print<<BLOCK;
<!DOCTYPE html>
<html><head><title>Resultado</title>
<body style="background:#f8b4de;">
<center>
<h1 style="color:black;">El resultado es: $resultado</h1>
<img src="https://static.vecteezy.com/system/resources/previews/001/200/261/non_2x/check-png.png" height="300"type="Google">
</center>
</body></html>
BLOCK
