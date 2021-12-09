create or replace function agentecadenas(varchar(20), varchar(20)) returns void as $$
declare 
  cadena1 alias for $1;
  cadena2 alias for $2;
  aux varchar(50);
  len1 int;
  len2 int;
  i int;
  letra1 varchar(1);
  letra2 varchar(1);
  sq text;
  _cantidad int;
  _posicion int;
  posi varchar(3);
  valor decimal(5,2);
  resultado decimal(5,2);
begin
	--ELiminamos la tabla
	drop table cadena;
	len1 := length(cadena1);
	len2 := length(cadena2);
	if len1 < len2 then
		len2 := len1;
		len1 := length(cadena2);
		aux := cadena1;
		cadena1 := cadena2;
		cadena2 := aux;
	end if;
	--En la cadena1 esta la cadena mas grande
	
  	i:=1;
  	sq := 'create table cadena (';
  	--Creamos la tabla de la cadena mas grande
	while i<=len1
  	loop
     	select substring(cadena1 from i for 1) into letra1;
     	sq := sq||letra1||i||' int,';
     	i:=i+1;
  	end loop;
  	sq := substring(sq from 1 for char_length(sq)-1);
  	sq:=sq||')';
	--Ejecutamos la creacion de la tabla
  	execute sq;
	
	--Insertamos la cadena menor
  	i:=1;
  	while i<=len2
  	loop
     select substring(cadena2 from i for 1) into letra2;
     --raise notice '%', letra2;
     
     select ordinal_position, count(*) as cantidad into _posicion, _cantidad 
	from information_schema.columns 
	where table_name='cadena'
	      and substring(column_name from 1 for 1)=letra2
	      and ordinal_position>=i
	group by ordinal_position
	LIMIT 1;
     if _cantidad>=1 then
        sq := 'insert into cadena('||letra2||_posicion||') values(1)';
        --insertamos 
		execute sq;
     end if;
     i:=i+1;
  end loop;
  
  --sumamos
  sq := '';
  i := 1;
  while i <= len1
  loop
  	select COLUMN_NAME into posi
	from INFORMATION_SCHEMA.COLUMNS
	where TABLE_NAME='cadena'
	and ORDINAL_POSITION = i;
	sq := sq || 'COALESCE(sum('|| posi || '),0)+';
	i := i+1;
  end loop;
  sq := LEFT(sq,length(sq)-1);
  sq := 'select ' || sq || ' from cadena';
  --raise notice '%',sq;
  execute sq into valor;
  --raise notice '%', valor;
  resultado := 0;
  --Verificar Ceros
  if valor = 0.00 then
  	--las cadenas son distintas
	raise notice 'Cadenas totalmente diferentes coincidencia 0';
  else
  	resultado := (valor/cast(len1 as decimal))*100;
  	raise notice 'Hay una coincidencia del % porciento', resultado;
  end if;
end;
$$
LANGUAGE plpgsql;


 --select agentecadenas('alejandra','pedro');
 --select agentecadenas('alex','alejandro');
select * from cadena;
--select * from cadena;
--drop table cadena;