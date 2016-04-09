var n,m,i,j,max,kolvo_max,str:integer;
    a:array [1..100,1..100] of integer;
    s:array [1..100] of integer;
begin
  readln(n,m);
  max:=a[1,1];
  kolvo_max:=0;
  for i:=1 to n do
    for j:=1 to m do
    begin
      read(a[i,j]);
      if (max<a[i,j]) then
      max:=a[i,j];
    end;
  for i:=1 to n do
  begin
    for j:=1 to m do
    if (max=a[i,j])and(str=0) then
    begin
      inc(kolvo_max);
      inc(str);
      s[i]:=i;
    end;
    str:=0;
  end;
  writeln(kolvo_max);
  for i:=1 to n do
    if (s[i]<>0) then
    write(s[i]-1,' ');
end.
