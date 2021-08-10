<?php

declare(strict_types=1);

interface Convertable {
    function convert(\SplFileObject $file, string $outputFormat, string $outputFilePath);
}

class CSVToJSON implements Convertable {
    function convert(\SplFileObject $file, string $outputFormat, string $outputFilePath) {
        echo "csv to json\n";
    }
}

class XMLToJSON implements Convertable {
    function convert(\SplFileObject $file, string $outputFormat, string $outputFilePath) {
        echo "xml to json\n";
    }
}

class JSONToXML implements Convertable {
    function convert(\SplFileObject $file, string $outputFormat, string $outputFilePath) {
        echo "json to xml\n";
    }
}

class Converter {
    private $converter;

    public function __construct(Convertable $converter) {
        $this->converter = $converter;
    }

    public function convert(\SplFileObject $file, string $outputFormat, string $outputFilePath)
    {
        // TODO implement it
    }
}

$converter1 = new Converter(new CSVToJSON());
$converter2 = new Converter(new XMLToJSON());
$converter3 = new Converter(new JSONToXML());


