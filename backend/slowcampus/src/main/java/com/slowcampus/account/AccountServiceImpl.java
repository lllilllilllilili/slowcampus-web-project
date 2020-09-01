package com.slowcampus.account;

import java.sql.SQLException;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class AccountServiceImpl implements AccountService{
	
	@Autowired
	AccountDao dao;

	@Override
	public AccountVO getUser(String user_id, String user_pw) throws SQLException {
		// TODO Auto-generated method stub
		return dao.getUser(user_id, user_pw);
	}
	
}
