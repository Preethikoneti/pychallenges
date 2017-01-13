$file = get-content C:\temp\temp.log
$previous = ""
$count = 0
$events = ""
foreach($line in $file){       
    $current = $line.Substring(1,12)
    if($previous -EQ "")
        {
         $previous = $current
         }
    if($current -eq $previous)
        {
         $count += 1
         }else{
            $events += $previous + "," + $count + "`n";
            $count = 1;
            $previous = $current
            }
}
$events += $previous + "," + $count
$events
["[' Jan 20 03:25']", '2']
["[' Jan 20 03:26']", '2']
["[' Jan 20 03:30']", '2']
["[' Jan 20 05:03']", '1']
["[' Jan 20 05:20']", '1']
["[' Jan 20 05:22']", '6']