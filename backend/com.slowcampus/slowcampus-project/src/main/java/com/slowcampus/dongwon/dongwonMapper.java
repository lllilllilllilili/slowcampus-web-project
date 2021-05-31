package com.slowcampus.dongwon;

import java.sql.SQLException;
import java.util.*;
public interface dongwonMapper {
	public ArrayList<dongwonVO> getInfo() throws SQLException;
}
