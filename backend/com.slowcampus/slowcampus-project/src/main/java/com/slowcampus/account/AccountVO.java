package com.slowcampus.account;

public class AccountVO {

	private String user_id;
	private String user_pw;
	private String user_job;
	private String user_name;
	private boolean status;
	
	public String getUser_id() {
		return user_id;
	}
	public void setUser_id(String user_id) {
		this.user_id = user_id;
	}
	public String getUser_pw() {
		return user_pw;
	}
	public void setUser_pw(String user_pw) {
		this.user_pw = user_pw;
	}
	public String getUser_job() {
		return user_job;
	}
	public void setUser_job(String user_job) {
		this.user_job = user_job;
	}
	public String getUser_name() {
		return user_name;
	}
	public void setUser_name(String user_name) {
		this.user_name = user_name;
	}
	public boolean isStatus() {
		return status;
	}
	public void setStatus(boolean status) {
		this.status = status;
	}
	@Override
	public String toString() {
		return "AccountVO [user_id=" + user_id + ", user_pw=" + user_pw + ", user_job=" + user_job + ", user_name="
				+ user_name + ", status=" + status + "]";
	}
	
	
	

}
