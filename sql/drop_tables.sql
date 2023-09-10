begin
  for rec in (SELECT
				table_name
			FROM
				all_tables
			WHERE
				OWNER ='IPEDS'
  )
loop
    execute immediate 'drop table ipeds.'|| rec.table_name;
  end loop;             
end;