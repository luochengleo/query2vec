@docs;
@docname;
$docname[0]="imine11.cn";

$len=1;

for($i=0;$i<$len;$i++){
	open (INFILE,$docname[$i]);
	while($line=<INFILE>){
		@arr=split(" ",$line);
		if(@arr>3){
			$docid=$arr[2];
			$docs[$i]{$docid}="unknown";
			#print "load $docid\n";
		}
	}
	close(INFILE);
}
$linecount=0;
$count=0;
$dir="/work/caoyj/SogouT/";
opendir(FIL,$dir);
@filename=readdir(FIL);
foreach $fn (@filename){
	if($fn=~/^SogouT/){
		$linecount=0;
		print ("process: $dir$fn\n");
		#open(PRE,$dir.$fn);
		open(PRE,"7zr x -so /work/caoyj/SogouT/".$fn." |");
		while($line=<PRE>){
			if($line=~/^\<DOCNO\>(.+?)\<\/DOCNO\>/){
				$linecount++;
				if($linecount%30000==0){
					print "doc $linecount\n";
					#last;
				}
				$id=$1;
				$content="";
				$flag=0;
				for($di=0;$di<$len;$di++){
					if(exists($docs[$di]{$id})){
						$flag=1;
					}
				}
				if($flag==0){
					next;
				}
				while($line=<PRE>){
					$line=~s/\s//gm;
					if($line=~/^\<\/DOC\>/){
						last;
					}
					$content=$content.$line;
				}
				for($di=0;$di<$len;$di++){
					if(exists($docs[$di]{$id})){
						print "find $id\n";
						$docs[$di]{$id}=$content;
					}
				}
			}
		}
		close(PRE);
		#last;
	}
}
#print "count= $count\n";
print "begin output\n";

for($i=0;$i<$len;$i++){
	open (INFILE,$docname[$i]);
	open (OUTFILE,">".$docname[$i].".content");
	while($line=<INFILE>){
		$line=~s/\n//;
		@arr=split(" ",$line);
		if(@arr>3){
			$docid=$arr[2];
			if(exists($docs[$i]{$docid}) && $docs[$i]{$docid} ne "unknown"){
				print OUTFILE ($line."\n".$docs[$i]{$docid}."\n");
			}
			else{
				print OUTFILE ($line."\n"."content not found\n");
			}
		}
	}
}
close(INFILE);
close(OUTFILE);