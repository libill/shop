<?php

define ('HAIER_URL', 'http://127.0.0.1');

define ("ERROR", serialize (array (

       // goods errors
       "6001" => "keyword,cid,sid cannot all be null!",
       "6002" => "iids,urls cannot all be null!",
       "6003" => "cids cannot be null!",

       //shops erors
       "7001" => "sids cannot be null!"

       )));


$error = unserialize(ERROR);


function echo_errors_and_exit($ret, $err_code, $err_msg='') {
  global $error;
  $ret['error_code'] = $err_code;
  if (strlen($err_msg) > 0) {
     $ret['error_message'] = $err_msg;
  } else {
     $ret['error_message'] = $error[$err_code];
  }
  echo(json_encode($ret));
  exit();
}
