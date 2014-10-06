<?php
namespace Grav\Common\GPM\Local;

use Grav\Common\Data\Data;

/**
 * Class Package
 * @package Grav\Common\GPM\Local
 */
class Package
{
    /**
     * @var Data
     */
    protected $data;
    /**
     * @var \Grav\Common\Data\Blueprint
     */
    protected $blueprints;

    /**
     * @param Data $package
     * @param bool $package_type
     */
    public function __construct(Data $package, $package_type = false)
    {
        $this->data       = $package;
        $this->blueprints = $this->data->blueprints();

        if ($package_type) {
            $this->blueprints->set('package_type', $package_type);
        }
    }

    /**
     * @return mixed
     */
    public function isEnabled()
    {
        return $this->data['enabled'];
    }

    /**
     * @return Data
     */
    public function getData()
    {
        return $this->data;
    }

    /**
     * @param $key
     * @return mixed
     */
    public function __get($key)
    {
        return $this->blueprints->get($key);
    }

    /**
     * @return string
     */
    public function __toString()
    {
        return $this->toJson();
    }

    /**
     * @return string
     */
    public function toJson()
    {
        return $this->blueprints->toJson();
    }

    /**
     * @return array
     */
    public function toArray()
    {
        return $this->blueprints->toArray();
    }
}
