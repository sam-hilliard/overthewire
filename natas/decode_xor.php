<?php
	$cookie = "MGw7JCQ5OC04PT8jOSpqdmkgJ25nbCorKCEkIzlscm5oKC4qLSgubjY%3D";
  $cookie = base64_decode($cookie);
  
  function get_key($in) {
    $key = json_encode(array("showpassword"=>"no", "bgcolor"=>"#ffffff"));
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
      $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
  }
  
  echo "key: " . get_key($cookie) . "\n";
  
  $magicCookie = json_encode(array("showpassword"=>"yes", "bgcolor"=>"#ffffff"));
  function getMagicTicket($in) {
    $key = 'KNHL';
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
      $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
  }
  
  echo "data: " . base64_encode(getMagicTicket($magicCookie));
?>
