<?php
echo "<pre>";
  // Get the search variable from URL

  $var = @$_GET['q'] ;
  $trimmed = trim($var); //trim whitespace from the stored variable

  $files = glob("./*.txt");
?>