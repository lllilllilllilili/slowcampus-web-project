package com.slowcampus.account;
import java.sql.SQLException;
import com.slowcampus.account.AccountVO;
public interface AccountService {
	public AccountVO getUser(String user_id, String user_pw) throws SQLException;
}

