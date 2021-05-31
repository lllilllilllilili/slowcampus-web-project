package com.slowcampus.dongwon;

public class dongwonVO {
	
	private String id;
	private String name;
	private String deptno;
	private String empno;
	
	
	public String getId() {
		return id;
	}
	public void setId(String id) {
		this.id = id;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getDeptno() {
		return deptno;
	}
	public void setDeptno(String deptno) {
		this.deptno = deptno;
	}
	public String getEmpno() {
		return empno;
	}
	public void setEmpno(String empno) {
		this.empno = empno;
	}
	
	@Override
	public String toString() {
		return "dongwonVO [id=" + id + ", name=" + name + ", deptno=" + deptno + ", empno=" + empno + "]";
	}
}
