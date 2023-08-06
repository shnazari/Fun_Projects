-- ============================================================================
-- ============================= Data Engineering =============================
-- ============================================================================

create table titles (
	title_id varchar(50) not null,
	title varchar(100) not null,
	primary key (title_id)
);


create table employees (
	emp_no varchar(50) not null,
	emp_title_id varchar(50) not null,
	birth_date Date not null,
	first_name varchar(100) not null,
	last_name varchar(100) not null,
	sex varchar(20) not null,
	hire_date date not null,
	primary key (emp_no),
	constraint fk_emp_title_id
		foreign key (emp_title_id)
			references titles (title_id)
);


create table salaries (
	emp_no varchar(50) not null,
	salary varchar(100) not null,
	primary key (emp_no)
);


create table departments(
	dept_no varchar(50) not null,
	dept_name varchar(100) not null,
	primary key (dept_no)
);


create table dept_emp (
	emp_no varchar(50) not null,
	dept_no varchar(50) not null,
	primary key (emp_no, dept_no),
	constraint fk_emp_no
		foreign key (emp_no)
			references employees (emp_no)
);

alter table dept_emp
	add constraint fk_dept_no
		foreign key (dept_no)
			references departments (dept_no)
;


create table dept_manager (
	dept_no varchar(50) not null,
	emp_no varchar(50) not null,
	primary key (emp_no),
	constraint fk_emp_no 
		foreign key (emp_no) 
			references employees (emp_no)
);

alter table dept_manager
add constraint fk_dept_no
	foreign key (dept_no)
		references departments (dept_no)
;
