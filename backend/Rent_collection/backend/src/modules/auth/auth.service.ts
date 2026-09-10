import bcrypt from 'bcrypt';
import { AuthRepository } from './auth.repository.js';
import { RegisterDto } from './dto/register.dto.js';
import generateToken from './helper/generateToken.js';

const SALT_ROUNDS = 12;

export class AuthService {
  constructor(private authRepository: AuthRepository) {}

  async register(dto: RegisterDto) {
    // 1. Business rule: no duplicate emails
    const existingUser = await this.authRepository.findByPhone(dto.phone);
    if (existingUser) {
      throw new Error('PHONE_ALREADY_EXISTS'); // handled by error middleware later
    }

    // 2. Hash the password — THIS is where hashing belongs
    const passwordHash = await bcrypt.hash(dto.password, SALT_ROUNDS);

    // 3. Persist via repository (repository never sees raw password)
    const user = await this.authRepository.create({
      name: dto.name,
      phone: dto.phone,
      passwordHash,
      role: dto.role === 'admin' ? 'ADMIN' : 'USER',
    });

    // 4. Never return the hash to the caller
    return {
      id: user.id,
      name: user.name,
      phone: user.phone,
      role: user.role,
    };
  }

  async login(phone: string, password: string) {
    try {
    const user = await this.authRepository.findByPhone(phone);
    if (!user) {
      throw new Error('INVALID_CREDENTIALS');
    }

    const isPasswordValid = await bcrypt.compare(password, user.password);
    if (!isPasswordValid) {
      throw new Error('INVALID_CREDENTIALS');
    }

   if (!user.isActive) {
      throw new Error('USER_NOT_ACTIVE');
    }

    const generatedToken = generateToken(user.id);
    return {
      token: generatedToken,
      message: 'Login successful',
    };
  } catch (error) {
    console.error('Error during login:', error);
    throw new Error('LOGIN_FAILED');
  }
}
}