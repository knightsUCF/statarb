{
    "method": "ftp",
    "host": "ftp.standardandpoors.com",
    "user": "limegrp",
    "pass": "sh3nd3r",
    
    "remote_dir": "/outbound/",
    "local_dir": "compustat/global_idhist",
    "regex": "idhist_intl\.zip",
    "flag": ".zip:.flg",
    "format": "compustat_idhist",
    "new_data_frequency": 24L*60L*60L*1000L,
}
