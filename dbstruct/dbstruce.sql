CREATE TABLE `course_video` (
  `video_id` char(32) NOT NULL COMMENT '视频id, 定长32字节的十六进制数值串, 可能为空串, 对应vhall的活动id',
  `activity_id` int(11) NOT NULL DEFAULT '0'
  `title` varchar(256) NOT NULL COMMENT '视频标题',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '最近修改时间',
  PRIMARY KEY (`course_id`,`lang_type`,`seq_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='课程的视频表';