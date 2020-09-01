package com.slowcampus.account;

import java.sql.SQLException;

public interface AccountMapper {
	public AccountVO getUser(String user_id, String user_pw) throws SQLException;

}
