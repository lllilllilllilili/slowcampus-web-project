package com.slowcampus.dongwon;

import java.sql.SQLException;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.*;
@Service
public class dongwonServiceImpl implements dongwonService{
	@Autowired
	dongwonDao dao;

	public ArrayList<dongwonVO> getInfo() throws SQLException {
		// TODO Auto-generated method stub
		return dao.getInfo();
	}
	
}
