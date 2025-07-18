def glBindAttribLocation(program, index, name): ...
def glBufferData(target, data, usage): ...
def glBufferSubData(target, offset, data): ...
def glCompressedTexImage2D(target, level, internalformat, width, height, border, data): ...
def glCompressedTexSubImage2D(target, level, xoffset, yoffset, width, height, format, data): ...
def glDeleteBuffer(buffer): ...
def glDeleteFramebuffer(framebuffer): ...
def glDeleteRenderbuffer(renderbuffer): ...
def glDeleteTexture(texture): ...
def glDrawElements(mode, count, type, offset): ...
def glCreateBuffer(): ...
def glCreateFramebuffer(): ...
def glCreateRenderbuffer(): ...
def glCreateTexture(): ...
def glGetActiveAttrib(program, index): ...
def glGetActiveUniform(program, index): ...
def glGetAttribLocation(program, name): ...
def glGetFramebufferAttachmentParameter(target, attachment, pname): ...
def glGetProgramInfoLog(program): ...
def glGetRenderbufferParameter(target, pname): ...
def glGetShaderInfoLog(shader): ...
def glGetShaderSource(shader): ...
def glGetParameter(pname): ...
def glGetUniform(program, location): ...
def glGetUniformLocation(program, name): ...
def glGetVertexAttrib(index, pname): ...
def glGetVertexAttribOffset(index, pname): ...
def glShaderSource(shader, source): ...
def glTexImage2D(target, level, internalformat, format, type, pixels): ...
def glTexSubImage2D(target, level, xoffset, yoffset, format, type, pixels): ...
def glVertexAttribPointer(indx, size, type, normalized, stride, offset): ...

# List of functions that we should import from OpenGL.GL
_functions_to_import: list = ...

# List of functions in OpenGL.GL that we use
_used_functions: list = ...
