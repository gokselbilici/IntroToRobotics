# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from tgr_msgs/VehicleMode.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class VehicleMode(genpy.Message):
  _md5sum = "0fa27dc54e25fb913feff0e9b007f61d"
  _type = "tgr_msgs/VehicleMode"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """bool mission
bool visial_guidance
bool obstacle_avoidance

int32 mode
"""
  __slots__ = ['mission','visial_guidance','obstacle_avoidance','mode']
  _slot_types = ['bool','bool','bool','int32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       mission,visial_guidance,obstacle_avoidance,mode

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(VehicleMode, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.mission is None:
        self.mission = False
      if self.visial_guidance is None:
        self.visial_guidance = False
      if self.obstacle_avoidance is None:
        self.obstacle_avoidance = False
      if self.mode is None:
        self.mode = 0
    else:
      self.mission = False
      self.visial_guidance = False
      self.obstacle_avoidance = False
      self.mode = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3Bi().pack(_x.mission, _x.visial_guidance, _x.obstacle_avoidance, _x.mode))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 7
      (_x.mission, _x.visial_guidance, _x.obstacle_avoidance, _x.mode,) = _get_struct_3Bi().unpack(str[start:end])
      self.mission = bool(self.mission)
      self.visial_guidance = bool(self.visial_guidance)
      self.obstacle_avoidance = bool(self.obstacle_avoidance)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3Bi().pack(_x.mission, _x.visial_guidance, _x.obstacle_avoidance, _x.mode))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 7
      (_x.mission, _x.visial_guidance, _x.obstacle_avoidance, _x.mode,) = _get_struct_3Bi().unpack(str[start:end])
      self.mission = bool(self.mission)
      self.visial_guidance = bool(self.visial_guidance)
      self.obstacle_avoidance = bool(self.obstacle_avoidance)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3Bi = None
def _get_struct_3Bi():
    global _struct_3Bi
    if _struct_3Bi is None:
        _struct_3Bi = struct.Struct("<3Bi")
    return _struct_3Bi