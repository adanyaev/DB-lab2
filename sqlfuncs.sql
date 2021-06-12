
create or replace function create_tables_and_triggers()
returns void
language sql as $$

	create table if not exists numbers 
	(
		Id SERIAL primary key,
		floor int,
		num_of_beds int,
		sea_view boolean,
		price int
	);

	create table if not exists people
	(
		Id SERIAL primary key,
		firstName text,
		lastName text,
		age int,
		phone_num text,
		email text
	);

	create table if not exists reservations
	(
		Id SERIAL primary key,
		human int references people(id) ON DELETE CASCADE,
		number int references numbers(id) ON DELETE CASCADE,
		dateFrom date,
		num_of_days int,
		price int,
		finished boolean
	);
	
	create index if not exists lastname on people (lastname);
		
	create or replace function count_price()
		returns trigger
		as $u$
		begin
			if TG_OP = 'INSERT' or 
			(TG_OP = 'UPDATE' and 
			 (NEW.num_of_days <> OLD.num_of_days or NEW.number <> OLD.number))
			then
				update reservations
				set price = reservations.num_of_days * numbers.price
				from numbers
				where number = numbers.Id;
				return new;
			end if;
			return new;
		end;
		$u$ language plpgsql;

	drop trigger if exists price_counter on reservations;
	create trigger price_counter after insert or update
	on reservations
		for each row execute procedure count_price();

		
	create or replace function fin()
		returns trigger
		as $u$
		begin
		if TG_OP = 'INSERT' or 
			(TG_OP = 'UPDATE' and 
			 (NEW.num_of_days <> OLD.num_of_days or NEW.number <> OLD.number))
			then
				update reservations
				set finished = TRUE
				where current_date - reservations.datefrom > reservations.num_of_days;
				update reservations
				set finished = FALSE
				where current_date - reservations.datefrom <= reservations.num_of_days;
				return new;
			end if;
			return new;
		end;
		$u$ language plpgsql;

	drop trigger if exists fin_check on reservations;
	create trigger fin_check after insert or update on reservations
		for each row execute procedure fin();
$$;

select create_tables_and_triggers();

create or replace function create_all_functions()
returns void
language sql as $u$
	create or replace function get_numbers()
		returns table (Id int,
						floor int,
						num_of_beds int,
						sea_view boolean,
						price int
		) language plpgsql as $$
			begin 
				return query select * from numbers;
			end
		$$;

	create function get_people()
		returns table (Id int,
						firstName text,
						lastName text,
						age int,
						phone_num text,
						email text
			) language plpgsql as $$
			begin 
				return query select * from people;
			end
		$$;

	create function get_reservations()
		returns table (Id int,
			human int,
			number int,
			dateFrom date,
			num_of_days int,
			price int,
			finished boolean
		) language plpgsql as $$
			begin 
				return query select * from reservations;
			end
		$$;

	create function clear_numbers() 
		returns void language sql as $$ 
			delete from numbers
		$$;

	create function clear_reservations()
		returns void language sql as $$ 
			delete from reservations
		$$;

	create function clear_people()
		returns void language sql as $$ 
			delete from people
		$$;

	create function add_to_reservations(human_id int, number_id int, datefrom_ text, num_of_days_ int)
		returns void language sql as $$
			insert into reservations(human, number, datefrom, num_of_days) values (human_id, number_id, cast (datefrom_ as date), num_of_days_)
		$$;

	create function add_to_people(firstname_ text, lastname_ text, age_ int, phone text, em text)
		returns void language sql as $$
			insert into people(firstname, lastname, age, phone_num, email) values (firstname_, lastname_, age_, phone, em)
		$$;

	create function add_to_numbers(floor_ int, beds_num int, sea boolean, price_ int)
		returns void language sql as $$
			insert into numbers(floor, num_of_beds, sea_view, price) values (floor_, beds_num, sea, price_)
		$$;

	create or replace function find_people(surname text)
        returns table (p_Id int,
                        firstName text,
                        lastName text,
                        age int,
                        phone_num text,
                        email text,
                       r_Id int,
                       human_id int,
                       number_id int,
                       datefrom date,
                       num_of_days int,
                       price int,
                       finished boolean
            ) language plpgsql as $$
            begin 
                return query select * from people
                left outer join reservations
                on people.id = reservations.human
                where people.lastname = surname;
            end
        $$;

	create function delete_people(surname text)
		returns void
		language plpgsql as $$
			begin 
				delete from people
				where lastname=surname;
			end
		$$;
		
	create function delete_reservation (id_ int)
		returns void
		language plpgsql as $$
			begin 
				delete from reservations
				where id=id_;
			end
		$$;

	create function delete_number (id_ int)
		returns void
		language plpgsql as $$
			begin 
				delete from numbers
				where id=id_;
			end
		$$;

	create function delete_human (id_ int)
		returns void
		language plpgsql as $$
			begin 
				delete from people
				where id=id_;
			end
		$$;

	drop function if exists find_apr_numbers_for_human;
	create or replace function find_apr_numbers_for_human (p_num int, datefrom_ text, d_num int)
		returns table (id int,
						floor int,
						num_of_beds int,
						sea_view boolean,
						price int
		) language plpgsql as $$
			begin 
				return query select numbers.id, numbers.floor, numbers.num_of_beds, numbers.sea_view, numbers.price
				from numbers left outer join reservations
				on reservations.number = numbers.id 
				where (reservations.finished = true or 
					   reservations.finished IS NULL or
					   reservations.datefrom + reservations.num_of_days < cast (datefrom_ as date)) and
				numbers.num_of_beds >= p_num;
			end
		$$;


	create or replace function find_apr_numbers ()
		returns table (id int,
						floor int,
						num_of_beds int,
						sea_view boolean,
						price int
		) language plpgsql as $$
			begin 
				return query select numbers.id, numbers.floor, numbers.num_of_beds, numbers.sea_view, numbers.price
				from numbers left outer join reservations
				on reservations.number = numbers.id 
				where (reservations.finished = true or reservations.finished IS NULL);
			end
		$$;
	
	create function update_reservations (id_ int, human_id int, number_id int, datefrom_ text, num_of_days_ int)
		returns void
		language plpgsql as $$
		begin
			update reservations
			set (human, number, datefrom, num_of_days) = (human_id, number_id, cast (datefrom_ as date), num_of_days_)
			where id_= id;
		end;
		$$;
	
	create function update_people (id_ int, firstname_ text, lastname_ text, age_ int, phone_num_ text, email_ text)
		returns void
		language plpgsql as $$
		begin
			update people
			set (firstname, lastname, age, phone_num, email) = (firstname_, lastname_, age_, phone_num_, email_)
			where id_= id;
		end;
		$$;
		
	create or replace function update_number (id_ int, floor_ int, num_of_beds_ int, sea_view_ boolean, price_ int)
		returns void
		language plpgsql as $$
		begin
			update numbers
			set (floor, num_of_beds, sea_view, price) = (floor_, num_of_beds_, sea_view_, price_)
			where id_= id;
		end;
		$$;
$u$;


select create_all_functions();
