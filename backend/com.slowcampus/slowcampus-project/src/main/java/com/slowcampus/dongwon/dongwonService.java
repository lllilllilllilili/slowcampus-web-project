package com.slowcampus.dongwon;
import java.sql.SQLException;
import com.slowcampus.*;
import java.util.*;
public interface dongwonService{
	public ArrayList<dongwonVO> getInfo() throws SQLException;
}