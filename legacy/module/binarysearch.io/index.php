<?php
    require_once dirname(__FILE__) . '/../../config.php';

    $url = 'https://binarysearch.io/api/contests';
    $json = curlexec($url, null, array("http_header" => array('content-type: application/json'), "json_output" => 1));

    $data_contests = array_merge($json['contests'], $json['eduContests']);
    foreach ($data_contests as $c) {
        if (empty($c['starting'])) {
            continue;
        }

        $contests[] = array(
            'start_time' => $c['starting'],
            'duration' => $c['contestDuration'] / 60.0,
            'title' => $c['name'],
            'url' => 'https://binarysearch.io/room/' . $c['uniqueSlug'],
            'host' => $HOST,
            'rid' => $RID,
            'timezone' => $TIMEZONE,
            'key' => $c['id'],
        );
    }

    if ($RID === -1) {
        print_r($contests);
    }
?>
