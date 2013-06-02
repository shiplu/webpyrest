create table langs(
	`lang_id` int not null auto_increment,
	`name` varchar(20) not null,
	-- A language may contain many types of properties. 
	-- It may not be consistent. So I am putting all of them 
	-- in one column as json.
	`data` text, 
	primary key(`name`),
	unique key(`lang_id`)
)Engine=InnoDB Default Character set utf8;