<?php
echo "<pre>";
  // Get the search variable from URL

  $var = @$_GET['q'] ;
  $trimmed = trim($var); //trim whitespace from the stored variable

  $files = glob("./*.{JPG,gif,png}", GLOB_BRACE);
  var_dump(basename($files[0],".JPG"));
?>