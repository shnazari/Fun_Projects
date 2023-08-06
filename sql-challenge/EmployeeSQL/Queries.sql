-- ============================================================================
-- ============================== Data Analysis ===============================
-- ============================================================================

-- 1. List the employee number, last name, first name, sex, and salary of each 
-- employee.
-- Tables to be queried: employees, salaries

select emp.emp_no "employee number", 
		emp.last_name "last name",
		emp.first_name "first name", 
		emp.sex, 
		sal.salary
from employees emp
left join salaries sal
	on emp.emp_no = sal.emp_no;


-- 2. List the first name, last name, and hire date for the employees who were 
-- hired in 1986.
-- Table to be queried: employees

select first_name "first name", 
		last_name "last name", 
		hire_date "hire date"
from employees
where date_part('year', hire_date) = 1986;


-- 3. List the manager of each department along with their department number, 
-- department name, employee number, last name, and first name.
-- Tables to be queried: dept_manager, departments, employees

select deptmgr.dept_no "department number",
		depts.dept_name "department name",
		emps.emp_no "employee number",
		emps.last_name "last name",
		emps.first_name "first_name"
from dept_manager deptmgr
left join departments depts
	on deptmgr.dept_no = depts.dept_no
left join employees emps
	on deptmgr.emp_no = emps.emp_no
;


-- 4. List the department number for each employee along with that employee’s 
-- employee number, last name, first name, and department name.
-- Tables to be queried: departments, employees, dept_emp

select depts.dept_no "departments number",
		emps.emp_no "employee number",
		emps.last_name "last name",
		emps.first_name "first name",
		depts.dept_name "department name"
from employees emps
left join dept_emp
	on emps.emp_no = dept_emp.emp_no
left join departments depts
	on dept_emp.dept_no = depts.dept_no
;
		

-- 5. List first name, last name, and sex of each employee whose first name is
-- Hercules and whose last name begins with the letter B.
-- Table to be queried: employees

select first_name " first name", 
		last_name "last name", 
		sex
from employees
where first_name = 'Hercules'and
		last_name like 'B%';


-- 6. List each employee in the Sales department, including their employee number,
-- last name, and first name.
-- Tables to be queried: employees, departments

select emps.emp_no "employee number",
		emps.last_name "last name",
		emps.first_name "first_name"
from employees emps
left join dept_emp
	on emps.emp_no = dept_emp.emp_no
left join departments depts
	on dept_emp.dept_no = depts.dept_no
where depts.dept_name ='Sales';

-- less efficient alternative query for this problem
-- using subqueries

select emp_no "employee number",
		last_name "last name",
		first_name "first_name"
from employees 
where emp_no in (select emp_no
				 from dept_emp
				 left join departments depts
				 	 on dept_emp.dept_no = depts.dept_no
				 where depts.dept_name = 'Sales'
);

-- 7. List each employee in the Sales and Development departments, including their 
-- employee number, last name, first name, and department name.
-- Tables to be queried: employees, departments, dept_emp

select emps.emp_no "employee number",
		emps.last_name "last name",
		emps.first_name "first_name",
		depts.dept_name "department name"
from employees emps
left join dept_emp
	on emps.emp_no = dept_emp.emp_no
left join departments depts
	on dept_emp.dept_no = depts.dept_no
where depts.dept_name in ('Sales','Development');


-- 8. List the frequency counts, in descending order, of all the employee last names
-- (that is, how many employees share each last name).
-- Tables to be queried: employees

select last_name "last name",
		count(last_name) count
from employees
group by last_name
order by count desc
;